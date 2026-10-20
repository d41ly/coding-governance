# Research: git and the memory outside the tracked files

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 107's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-10-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md`.

---

1. **Verdict**

Use typed commit trailers to join git to P33, with their inverses derived into the one index. Four mechanisms compete, and three lose a measured test:
- **Git notes** do not reach a plain clone and are dropped by rebase and cherry-pick.
- **A derived index alone** finds only citations: the SHAs that records name are measurement pins, not authorship.
- **Landing and transition records alone** cannot reach an item or a session.

Gov already runs two typed trailers: `Pass:` on 1,353 commits and `Decided:` on 677, both read through git's own parser. Today none of 6,084 commits carries an item, act, session or agent key. From one commit, the cycle reaches 3 of its 7 targets by key; the other 4 need search or prose. The outside pockets are inventoried below, and none of them has a record kind among the map's 70.

2. **Git as memory**

**Measured** (HEAD `78797c5f7`; the probes are under `…/scratchpad/away/d107/`):

```
$ git rev-list --count HEAD → 6084 · --no-merges 5544 · --merges 540
$ git log --format=%s | grep -cE '^[a-z-]+\([^)]+\)!?: '            → 4349 kind(scope):
  scope is a build slug                                              → 3309 (54.4%)
  FAMILY-slug-N id in subject                                        → 2959 (48.6%); subject ∪ Pass: → 2965
$ git log --format='%(trailers:only,unfold)' | key count
  Co-Authored-By 5792 · Decided 1516 (on 677 commits) · Pass 1353 (839 = none) · manifest-audit 20 · Spec 2 · Bar 2
  Co-Authored-By values: Opus 5 3604 · Opus 5.5 2082 · Fable 5 42 · Opus 5.5 (1M) 32 · Opus 4.8 32
  messages holding a UUID 1 · agent_id 0 · task-sha 2 · a [tag] in the subject 8 · notes 0
$ git for-each-ref (beyond heads/remotes) → refs/gov/remote/runs/* 17 · refs/tags/archive/* 3 (remote: refs/gov/runs 17, archive tags 6); no refs/gov/bar-red now
this branch: 196 commits, 196 name dClosedLoop, 0 a unit id, 0 Pass:, 0 Decided:
```

- **The ids are ambiguous.** Ask ids and unit ids share one grammar (`TOOL-aBoundedCeiling-8` is an ask in `memory/backlog/TOOL.md`), so a subject's id cannot be typed as a unit or an ask by its syntax.
- **Readers already exist.** `Pass:` is read by `routed_commits.py:222` and `check-unattended.sh:4210`. `Decided:` is read by `runlog/model.py:599` and instructed by `BUILD-METHOD.md:318`.
- **The two `Pass:` readers disagree.** One takes the union of the subject's ids and the trailer's; the other lets the trailer replace the subject (`routed_commits.py:22-25`).
- **The only git object that carries a session today** is the run-claim commit (`session: <uuid>`, `unattended.sh:2407-2412`, from `CLAUDE_CODE_SESSION_ID`). It is pushed to `refs/gov/runs/<slug>` and never deleted: no delete is found in `unattended.sh`, and 17 claims remain, landed ones included.

**Probe** (a bare remote plus clones, git 2.54):

| Operation | `Gov-*` trailer | `git notes` |
|---|---|---|
| reader by key (`%(trailers:key=Gov-Unit,valueonly)`), `--grep='^Gov-Unit: X$'`, `interpret-trailers --parse` | all three work | n/a |
| default push, then a plain clone | survives (`55065a6 TOOL-dX-2 s2`) | **0 notes** |
| notes pushed by refspec, then a plain clone | — | **0**; 2 only after `fetch 'refs/notes/*:refs/notes/*'` |
| rebase | survives | **lost**; kept only with `notes.rewriteRef` set |
| cherry-pick, and `-x` | survives | **lost** |
| `--no-ff` merge (gov's form, `push-main.sh:878`) | on the second parent; the walk finds 2 of 2 | — |
| squash with git's default message | **0 parsed**; 2 indented raw lines | lost |

Gov already refuses squash and rebase by instruction. `pre-rebase:5-8` blocks a rebase; squash and cherry-pick are named as unguarded, with the merge bar as the binding check. Inside a subagent the shell sees the parent's `CLAUDE_CODE_SESSION_ID` (`1799cb98…`) and no agent-id variable. An agent's own shell therefore cannot name its agent, but the supervisor that launched it can.

**The candidates:**

| | **T: typed trailers (pick)** | **N: git notes** | **D: derived commit index** | **L: landing and transition records only** |
|---|---|---|---|---|
| Mechanism | the commit is the site that owns "who made me": one trailer key per declared edge | edges attached to the commit in `refs/notes/gov` | rows built from records and the journal that name SHAs | the build-level records keyed by SHA |
| Syntax | `Gov-Unit: <id>` · `Gov-Item: <item>#<round>` · `Gov-Act: <act-key>` · `Gov-Session: <harness>:<id>` · `Pass:` and `Decided:` kept as registered keys | `gov: made-by=act:… runs-in=session:…` | `<git-common-dir>/gov/index` rows | landing: SHA, builds, units, verdict (`flow.md:492-493`) |
| Writer | the supervisor's commit queue, from the act binding (witnessed; `layer-runtime.md:695`). In the owner's session, a `prepare-commit-msg` hook fills `Gov-Session` from the environment | any process | generator | `deploy.record`, the transition items |
| Checker | a leg extending `routed_commits.py` at the push, reading the binding record rather than the trailer's writer ([class]) | a refspec check on every clone | re-render | the record checks |
| Survives | clone, push, rebase, cherry-pick, `--no-ff`; **not squash** | needs refspec, rewrite and merge config on every clone; a shared mutable ref across nodes | the tracked records survive, but the journal is per clone (`.git/runlog/`) | yes |
| Cost | about 4 lines per commit, one git call to read; the `commit-msg` seam exists (`.githooks/commit-msg:30-63`) | config on every node and adopter, plus notes merges | none to write | none |
| **Losing test** | a key lost through gov's integration paths, or unreadable by key | absent from a plain clone after a push | ≥80% of a branch's commits typed to an act or session by the records | an in-branch commit reaches its item and session |
| **Result** | **Passes** (table above). Squash is lost and becomes an adopter fork | **Loses**: 0 notes in a plain clone, lost on rebase and cherry-pick | **Loses**: 52.4% of commits are named somewhere, but both records naming `7788ac269` name it as a pin ("Derived at", `walk.md:518,1424`). No record names a session, and a commit cannot name itself | **Loses**: the landing record holds builds and units, not items or acts. The 196 unlanded commits reach nothing |

- **`Gov-Tags:` is rejected.** A commit's tags derive from its diff through `part-of`, so a typed list breaks [memory].
- **D stays as T's derived inverse,** the `cited-by` and `pinned-by` view.
- **Five is enough.** A YAML block in the commit body differs from T only in detail.

**Where record and code disagree:**
- The charter fact "every agent commit ends with `Co-Authored-By: Claude Opus 5`" holds for 3,604 of 6,084 commits; five model strings are in use.
- `flow-steps.md:253` names "the trailer … schemas", and `flow.md:363` says "the unit id and its trailers", but no kind among the 70 declares one.

3. **The other pockets**

| Pocket | Where; what writes it; what reads it | Key; lifetime | Joined today | Place on the map | Verdict |
|---|---|---|---|---|---|
| Auto-memory | `~/.claude/projects/C--projects-coding-governance/memory/`, 88 files and a 15.5 KB index. One per repo root: 1 of 41 project dirs has it. Written by agents, loaded by the harness | `name`; front matter `name/description/metadata{type,originSessionId,node_type,modified}` (87/88). Per machine, until deleted | `originSessionId` 79/87. 57 name a slug and 19 an id, in prose | dTotalRecall budgets "the auto-memory's remainder"; MS-1 promotes its directives. **No kind** | **Witness**: claimed, one machine, never a node. Its rows are extracted with their session key |
| Transcripts | `~/.claude/projects/<cwd>/<sid>.jsonl` plus `<sid>/subagents/agent-<id>.jsonl`. 3,910 here, 3,844 of them subagent. Written by the harness; read by SubagentStop (`layer-runtime.md:538`) and `runlog/extract.py` | `sessionId`, `uuid`, `agentId`, `gitBranch`, `cwd`. `cleanupPeriodDays: 365` (`~/.claude/settings.json:2`); oldest 2026-08-24 | commit to session only by search: 52 of 196 branch commits, each in more than one file | session binding (dWellOiledMachine) names the session but not the path | **Witness**: the binding record carries `transcript=` as a pointer |
| Orientation cards | `<git-common-dir>/orientation/<sid>.md`, 22. Written by `manifest-check.sh --card --write` (`scratch-guard.js:52`); read by format-guard (`hooks/README.md:428`) | the session id; current state, per clone | `## route`: `- build:` and `- unit:` | superseded by the session binding | **Node** as `session-binding`; the card retires |
| Run claims | remote `refs/gov/runs/<slug>`, 17 (`unattended.sh:2411`) | slug; never deleted | session, node, host, status | `claim`, `lease` | **Node**. Its `session:` becomes a `runs-in` edge |
| Runlog | `.git/runlog/{driver,gates,pushes}.log` | `slug` (1,964 lines), `unit` (368), `head`, `ref.N`; no session; no rotation found in `runlog.py` | slug, unit, SHA | `journal` (dWellOiledMachine), `runtime.journal` retention | **Node** as the journal, with `session=` and `act=` added |
| Health log | `<git-common-dir>/health.log`, bounded by halving (`reap.py:35-41`) | time, source, event | nothing | **gap** | **Witness** for the Maintain detectors |
| Gate ledger, logs, cache; review-lens cache; transition-audit cache | `.git/gate-ledger.tsv` (leg, secs, ok, tree SHA); `gate-logs` 123; `gate-cache` 319; `review-lenses` 145, keyed by range SHAs | tree or range SHA; overwritten | SHA | `verdict` (dWitnessedBar) | **Out**: caches. The verdict record is the node |
| Unattended sidecars | `.git/unattended/{<slug>.lease, .procs, landed.<slug>.log, stall.<slug>.log}` | slug | the landed SHA | lease, landing, journal | out: folded into those kinds |
| Agent-cap slots; recall index (462 MB); map cache | `.git/agent-cap/<sid>__<id>/slot-N`; `.git/recall`; `.git/codebase-map` | session; tree | — | Runtime mechanics; recall-index | **Out**: derived, re-rendered |
| Harness prompt history; file checkpoints | `~/.claude/history.jsonl` (`project`, `sessionId`); `~/.claude/file-history/` (75 sessions) | session | — | the `intake` record supersedes it | **Out** |
| Scheduled tasks | `~/.claude/scheduled-tasks` (12 tasks, 0 for gov); OS scheduler (`schtasks`: 0 gov tasks on node d) | name | — | the cadence witnesses and scheduler adapters (dWellOiledMachine) | **Witness**: the registration is read by preflight |
| Published artifacts | the atlas at a claude.ai artifact URL (`atlas-instruments.md:16-17`), published by hand | URL | nothing records which tree was published | **gap** | **Node**: a `release` per (SHA, environment `artifact:<url>`), reusing dShippedRelease's kind |
| Pull requests, issues, CI logs | none in use: 0 PR references in 6,084 subjects; `gh` is absent; remote CI is unavailable | — | — | `integrations.tracker: mirror-out`, emitted CI (dShippedRelease) | **Out** for gov; for adopters, a witness through an adapter row |

4. **The cycle**

The walk starts from `7788ac269` ("records(dClosedLoop): WK-3 priced…"). Its only trailer is `Co-Authored-By`.

| Hop | How it is reached | Keyed? |
|---|---|---|
| commit → build `dClosedLoop` | the subject's scope, a convention no hook checks | **key** (unchecked) |
| build → unit `PLAY-dClosedLoop-1` | README `ids:` (the build has one unit) | **key** |
| record touched → unit | `**Serves:** research PLAY-dClosedLoop-1` (`wk3-pricing.md:3`; 2,293 such lines) | **key** |
| commit → item and role | no field; "the walk's wave fold" is prose | **prose** |
| commit → session | full-text `7788ac269` across transcripts: one top-level file (`committed —` microformat, ×2) plus 5 subagent files that hold it as a pin | **search** |
| session → agent | `Co-Authored-By` names a model; `agentId` exists only in transcripts | **search** |
| commit → decision WK-3 | grep finds WK-3 defined at `night-pass-instruments.md:5083` and in the walk record; inside the record, `[wave-2-answers]` is a tag citation | **search**, then a key |
| commit → instruction | the owner's words are verbatim in the transcript and the walk record; a research return names its prompt by path in prose, and the prompt's `gov:handoff` header carries `role`, `unit`, `task-sha` and `role-sha` (62 of 74) | **prose**, then a key |

That is 3 keyed hops and 4 that need search or prose. With T, the `Gov-Act` trailer leads to the act record, which holds item, role, epoch, `task-sha` and session. One key chain then reaches all seven.

**Edges the closed set lacks:**

| Edge | Inverse | From → to | Declared at |
|---|---|---|---|
| `made-by` | made | commit or record → act | the `Gov-Act:` trailer; the record's writer |
| `runs-in` | hosts | act or claim → session | the session binding; the claim's `session:` |
| `follows` | followed-by | act → work order (`task-sha`) → instruction units | the spawn marker; `gov:handoff` |
| `pinned-at` | pinned-by | record, probe or claim → commit or tree | "Derived at", P31 pins; today these fall into `cites` |
| `carries` | carried-by | landing → unit and commit | the landing record |

Two existing edges need wider targets:
- `part-of` must reach a unit or a build, for `**Serves:**`.
- `decides` must reach a commit or an item, for `Decided:`.

5. **Chain, gaps and forks**

| Build | Units |
|---|---|
| dOrderedCharter | the five edge types and the two target widenings in the edge registry; the `commit` and `session` node namespaces' grammar |
| dDeclaredLoop | the `commit` kind: the trailer key set (`Gov-Unit`, `Gov-Item`, `Gov-Act`, `Gov-Session`, with `Pass` and `Decided` as registered keys), one reader replacing the union and replace split (`routed_commits.py:22-25`), and the position engine reading it; the leg extending `routed_commits.py`, its check fed by the binding record. Each arm must be seen red on a planted commit |
| dWellOiledMachine | the commit queue writing the trailers from the act binding; a `prepare-commit-msg` filler for the owner's session; `session=`, `act=` and `commit=` on journal lines; `transcript=` on the binding; the `session` namespace registered |
| dTotalRecall | the trailers extracted into the one index with their inverses (D as a view); the `commit` namespace; pocket rows in the kind registry for out-of-tree witnesses (home, reader, retention, join key); auto-memory front-matter rows, classed claimed |
| dLinkedLibrary | `Decided:` trailers read as decision rows (677 commits) |
| dShippedRelease | `carries=` on the landing record; an artifact publication as a `release` per (SHA, environment) |
| dTendedCadence | detectors over the health log and the runlog; a detector for commits missing a required key |

**Gaps to register:**
- **No commit edge.** 0 of 6,084 commits name an item, act or session, and the trailer schema is named but declared nowhere. Owner: dDeclaredLoop.
- **Two `Pass:` semantics.** Owner: dDeclaredLoop.
- **Session ids missing.** The journal and runlog carry none (all three logs). Owner: dWellOiledMachine.
- **Out-of-tree pockets have no kind or pocket row.** Owner: dTotalRecall.
- **Pins are typed as `cites`.** Owner: dOrderedCharter.
- **Publications go unrecorded.** Owner: dShippedRelease.
- **Squash drops trailers.** This is the adopter-portability gap. Owner: dShippedRelease.

**The owner's forks:**

| Fork | Options, recommendation first |
|---|---|
| GJ-1 Git's join | **typed trailers, inverses derived**; notes; a derived index only; landing and transition records only |
| GJ-2 Trailer shape | **one key per edge, mapped in the registry** (git filters by key, as `Pass:` and `Decided:` already show); one `Gov-Edge: type=target` key |
| GJ-3 Writer | **the commit queue from the binding, witnessed; a hook filler in the owner's session**; agents type them (claimed, under P23) |
| GJ-4 Enforcement | **written by the queue or hook, checked at the push by a leg reading the binding**; refused at `commit-msg` |
| GJ-5 Squash at adopters | **the lander re-emits the union of the trailers on a squash**; refuse squash; accept the loss |
| GJ-6 Auto-memory and transcripts | **witnesses with keyed pointers**; nodes; out |

The probes wrote only under `…/scratchpad/away/d107/` (`probe/`, `subjects`, `hex.txt`, `rk.txt`). No file in the repository changed.
