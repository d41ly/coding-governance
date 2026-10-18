# The instruction and memory plan: one practice, one syntax, every pocket

**Serves:** research PLAY-dClosedLoop-1

The owner's second point of the away pass asked for a full instruction and memory plan, its integrations into the
new architecture explained, laid down before the build proceeds. Its first point gave the plan's direction: memory
and instruction follow one writing practice, unified through one relational syntax and the tag system; every piece
joins, none is left to prose; and the whole relates cyclically through the syntax
(`build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md` `[words]`). This record is that plan. It rests on four
research returns, each saved verbatim: the repository's memory (`research-memory-pockets.md`, dispatch 106), git and
the memory outside the tracked files (`research-git-pockets.md`, 107), the harness and its session ids
(`research-harness-cli.md`, 108), and tracing what happened (`research-observability-trace.md`, 110). Its forks are
parked in the away-pass record's `[forks]`, each named there by its AP id.

## [frame] One graph, written one way

The layers already form a cycle: instruction says, runtime enforces, flow witnesses, memory proves
(layer-instruction `[layers]`). Instruction directs the flow, the flow names items, roles perform them, their
returns become memory, and memory renders the card and every work order. The plan makes that cycle one graph:
- **Every piece is a node.** A node has an address: a tag (`<ns>.<seg>`), a section (`<doc> [<seg>]`), or a native
  id (a commit's SHA, an id `FAMILY-<slug>-<seq>`, a gap key, an act id). Instruction units, record sections, code
  regions, commits, acts and sessions are all nodes of one index, resolved by one resolver.
- **Every relation is a typed edge.** Its type comes from one closed set, it is declared once at the site that owns
  its fact, and its inverse is derived (P33). A reference written as prose is a derived `cites`, never a typed fact.
- **Instruction and memory differ in level and lifecycle, never in grammar.** An instruction unit sits at levels 0
  to 6 and directs. A memory node sits at level 7 and proves. Memory instructs only through promotion, which leaves
  a `promoted-from` edge (P30, R-H).
- **What lives outside the tree joins by key.** A pocket the loop does not own, such as a transcript or the
  auto-memory, is a declared witness: the registry names its home, its key and its reader, and a node in the tree
  carries the pointer.

Today one family of typed links works end to end: the `**Serves:**` line, on 2,278 records, its inverse derived and
graded both ways (`research-memory-pockets.md` section 1). Of the twelve hops that trace one feature, seven are
typed and five need prose or search. From one commit, three of seven targets are reached by key
(`research-git-pockets.md` section 4). The plan closes every hop.

## [families] The memory's families

Eight families group every pocket, drawn as the atlas's memory view draws them.

| Family | Level | What it holds | Lifecycle |
|---|---|---|---|
| instruction | 0 to 6 | the charter, policy values, protocol slices, Skills and path rules, role static blocks, the card, work orders, reuse entries | rendered from units; edited only through `instructions.edit` |
| trail | 7 | one build's records: README, specs, design records, research returns, reviews, transitions, verdicts, landings, runs, asks | append-only or frozen at a transition, written through `record` |
| library | 7 | what generalizes beyond a build: decisions, bug classes, research, dossiers, the lexicon | current-state, written through `record`; consulted, never loaded as instruction |
| code | 7 | the code record, `gov:` annotations, tests, kits, legs, hooks | derived from the tree by hash; annotated by builders |
| git | 7 | commits, their messages and trailers, refs (claims, runs, mail, bar-red), tags (kit releases) | immutable once pushed; refs move by compare-and-swap |
| runtime | 7 | acts, session bindings, the journal, the inbox, and the harness stores the bindings point at | node-local, kept for `runtime.journal` |
| views | 7 | what is generated: LIVE.md, the ledger, ask views, the map, the recall index, the atlas | re-rendered, never merged |
| outside | 7 | what lives beyond the repository and the node's runtime: published artifacts, remote pull requests, issues and CI | read through an integrations adapter |

## [pockets] Every pocket, and its place

Each pocket is a node, a witness, or out. A node is declared in the kind registry and written through its door. A
witness is a pocket another writer owns, joined by a key a node carries. Out means a cache or a mechanic that no
reader needs. The counts are the returns' measurements.

| Pocket | Family | Where | Today | Becomes | Key | Owner |
|---|---|---|---|---|---|---|
| charter | instruction | `AGENTS.md`, rendered from the template | 45 rule tags; 0 of 9 headings tagged | node: units at level 0, `practice.<tag>` | tag | dOrderedCharter |
| policy values | instruction | the policy file, and today each kit's conf | keys typed per kit | node: units at level 2 | `policy.<key>` | dDeclaredLoop |
| protocols and guides | instruction | `memory/guides/`, `HYGIENE.md`, `TEMPLATE-SPEC.md` | 0 of 138 headings tagged; positional citations by number | node: protocol slices at level 3 | `doc.<name> [<seg>]` | dConvergedCharter |
| kickoff manifest | instruction | `memory/guides/SESSION-KICKOFF.md` | no kind and no unit | node: units at level 2 that the card reads | tag | dPlacedRequest |
| Skills and path rules | instruction | `.claude/skills/`, `.claude/rules/` | 0 tagged | node: thin entries at level 4 | tag | dConvergedCharter |
| role definitions | instruction | `tools/roles/agents/`, `.claude/agents/` | typed `reads:`, `writes:` and `rules:` fields | node: static blocks at level 5; `reads` and `writes` edges | `role.<name>` | dBoundRoles |
| work orders and handoffs | instruction | `memory/builds/*/prompts/` | the `gov:handoff` marker on 59 of 595 | node: level 6, every one marked | marker path, `task-sha` | dBoundRoles |
| the card | instruction | per build, rendered | per-session cards in the git dir today | node: level 1 | build | dPlacedRequest |
| reuse entries | instruction | the library's promoted units | none yet | node: level 3, `promoted-from` its source | tag | dLinkedLibrary |
| build README | trail | `memory/builds/*/README.md` | front matter on 167 of 167 | node | build slug | dTotalRecall |
| specs | trail | `memory/builds/*/spec/` | id and status lines; 0 tagged headings | node | unit id | dIndexedDesign |
| design and build records | trail | `memory/builds/*/build/` | Serves line; tagged headings in dClosedLoop only | node, every section an edge site | `<doc> [<seg>]` | dTotalRecall |
| research returns | trail | `research-*.md` | Serves line; the handoff named in prose | node: `answers` its work order | `<doc>` | dLinkedLibrary |
| reviews | trail | `memory/builds/*/reviews/` | Serves line | node | `<doc>` | dFairHearing |
| per-build asks | trail | `memory/builds/*/BACKLOG.md` | id on every row | node | ask id | dTotalRecall |
| run records | trail | `RUN*.md` | path only | node: the run record | run key | dTendedCadence |
| session logs | trail | each build's session log | dispatch rows and events | node: its events join acts by key | `<doc> [<seg>]` | dTotalRecall |
| decisions | library | `memory/DECISIONS.md` | 200 rows with ids; a relation word on 1, a feature edge on 0 | node: `decides` on every row | decision id | dLinkedLibrary |
| bug classes | library | `memory/gotchas/` | front matter on 148 of 149; `from:` on 0 | node: `caused-by` its finding | class tag | dLinkedLibrary |
| dossiers | library | `memory/map/features/` | claims gated 120 of 120 | node (optional component) | `feature.<name>` | dTotalRecall |
| lexicon | library | `tools/lexicon/`, `.lexicon.conf` | declaration only | node (optional component) | tag | dMindYourWords |
| code record | code | derived from the tree (P32) | the map's symbols | node: definitions with ranges | path and symbol | dTotalRecall |
| annotations | code | `gov:note`, `gov:feature` in code | 0 `gov:feature` lines; 20 marker words registered | edge site: `part-of`, `implements` | tag | dLinkedLibrary |
| commits | git | the history | 6,084; `Pass:` on 1,353 and `Decided:` on 677; none names an item, act or session | node, its trailers an edge site | SHA | dDeclaredLoop |
| refs | git | `refs/gov/claims`, `runs`, `mail`, `bar-red` | 17 run claims, never deleted | node: claims, leases, mail | ref name | dPlacedRequest |
| tags | git | kit releases, archive tags | 3 archive tags | node: `kit-release` | tag name | dShippedRelease |
| acts and session bindings | runtime | written by the supervisor | designed | node: the act carries item, work order, harness, harness session and node | act id | dWellOiledMachine |
| journal | runtime | `.git/runlog/` | slug on every line, unit on 368 of 1,964, session on none | node-local node: every line keyed by act or session | act id | dWellOiledMachine |
| health and stall logs | runtime | the git dir | no key | folded into the journal grammar | act id | dWellOiledMachine |
| Claude transcripts | runtime | `~/.claude/projects/<cwd>/<id>.jsonl` and `subagents/` | keyed by session and agent id; kept 365 days | witness: the binding's `transcript=` pointer | harness session id | dWellOiledMachine |
| Codex rollouts | runtime | `~/.codex/sessions/.../rollout-<ts>-<id>.jsonl` | `session_meta.id` on every file | witness: the binding's `transcript=` pointer | harness session id | dWellOiledMachine |
| the live inbox | runtime | the harness's per-session inbox | Claude only; addressed by session id | witness: live delivery beside the mailbox | harness session id | dWellOiledMachine |
| auto-memory | runtime | `~/.claude/projects/<repo>/memory/` | 88 files; `originSessionId` on 79 | witness: its standing directives promoted, its rows claimed | `name` | dTotalRecall |
| orientation cards | runtime | `<git-common-dir>/orientation/<id>.md` | 22, one per session | retired into the session binding | — | dWellOiledMachine |
| scheduled tasks | runtime | the OS scheduler, the harness's task list | 0 for gov | witness: read by preflight | task name | dWellOiledMachine |
| gate ledger, logs and caches | views | the git dir | keyed by tree or range SHA | out: the verdict record is the node | — | dWitnessedBar |
| LIVE and the ledger | views | `memory/LIVE.md`, `memory/ledger/` | generated | node: a view kind | — | dTotalRecall |
| ask views | views | `memory/backlog/*.md` | generated | node: a view kind | — | dTotalRecall |
| project registries | views | `memory/project/*.txt` | 872 path-keyed rows | node: the `registry` kind | path | dTotalRecall |
| archive | views | `memory/archive/` | rotated records | node: the `archive` kind | path | dTotalRecall |
| instruments | views | scripts and tables in build folders | 94 files; 3 carry no Serves line | node: the `instrument` kind | path | dTotalRecall |
| recall index | views | the git common dir | derived | node: `recall-index` | — | dLinkedLibrary |
| the map and the atlas | views | the level-0 map; the atlas, a published artifact | the atlas published by hand, its tree unrecorded | node: a publication is a `release` per (SHA, artifact environment) | URL | dShippedRelease |
| pull requests, issues, CI | outside | the remote | none in use by gov | out for gov; a witness through an adapter row for an adopter | — | dShippedRelease |
| prompt history and checkpoints | outside | the harness's own stores | keyed by session | out: the intake record supersedes them | — | — |

Two names collide today. "journal" is both a Serves kind on 1,436 records and Runtime's journal record kind; the
Serves kind is renamed `log` when dTotalRecall's registry lands.

## [practice] One writing practice

Every rule applies to an instruction unit and to a record section alike. Each has its check.

| Rule | What it asks | Check |
|---|---|---|
| address | a node is named by its tag, its section or its native id, never by position | `positional` (tags pack), shrink-only over today's population |
| one subject | a unit or a section holds one subject, and its tag is unique in its document | `unique` |
| typed relations | every relation to another node is an edge of a registered type, declared once at the site that owns the fact | the edge checks: type registered, target resolves, from and to namespaces allowed, inverse rendered |
| pinned facts | a quoted derived fact (a count, a size, a path's length) carries its pin on its line: a SHA or a cited line | `pinned-at`; the map's no-stale-facts arm, generalized from the design records to every record |
| statement types | loaded text is one of P11's six statement types; a record's prose is evidence and never loads | statement-type check on loaded units only |
| rationale apart | why a unit says what it says lives in its `help` field; a record keeps its reasoning in its own sections | render parity: `help` never renders into a load set |
| one door | each site has one writer: `instructions.edit`, `record`, the commit queue and its hook, the handoff renderer, the supervisor | render parity and the record check; a write elsewhere reds |
| one owner | every node names one owning build or layer | `owned` |
| retire, never vanish | a retired node leaves `retired → <new>` and its tag is never reused | `retired` |
| levels decide | a conflict resolves by level; memory at level 7 never instructs | the envelope (P13); promotion only through `instructions.edit` |

The shared grammar of an edge, at every site: `type=target[,target]`.

## [sites] Where each edge is declared

| Site | Syntax | Door |
|---|---|---|
| a record's header | `**Serves:** <kind> <unit>`, as today; `**Made-by:** <act or owner>`; `**Caused-by:** <id>` | `record` |
| a record's section | the `## [tag] Title` heading, then at most one line `**Edges:** type=target type=target` | `record` |
| an instruction unit | its row's `select`, `required-by` and `enforced-by` fields, as today, and `edges` in the same grammar | `instructions.edit` |
| code | `gov:note <tags> — <definition> → <pointer> [refs=…]` and `gov:feature <tag>` | the builder, under the annotation grammar |
| a commit | one trailer key per edge: `Gov-Unit:` and `Gov-Item:` for `serves`, `Gov-Act:` for `made-by`, `Gov-Session:` for `runs-in` as `trace.identity` says, with `Pass:` and `Decided:` kept as registered keys, each mapped to its edge type in the registry | the commit queue from the act binding; a `prepare-commit-msg` filler in the owner's session |
| a work order | the `gov:handoff` marker (role, build, unit, path, `role-sha`, `task-sha`), gaining `item=` | the handoff renderer |
| an act | the act record's fields: item instance, work order `task-sha`, harness, harness session, node, parent | the supervisor |
| a kind's registry row | its writer and readers | dTotalRecall's registry |

An edge line is one line under its heading, a median of 40 B, measured as an upper bound over today's records; a
section with more types than fit takes one line per type (`research-memory-pockets.md` section 3). The other three
placements each lost a measured test there: a section as a 200 B unit fits 7.3% of sections; front matter keyed by
section strands 43 of 45 multi-section records' facts away from their sections; a sidecar list kept apart drifted
in 12 of 31 dossiers.

## [edges] The closed set, extended

The twelve declared types stand (P33). Eleven join them, each needed by a hop the returns measured. `cites` stays
derived.

| Edge | From → to | Declared at | Inverse, derived | Status | Needed by |
|---|---|---|---|---|---|
| `part-of` | member → feature, kit, tag | annotations, dossier claims | `has-part` | P33 | the code's place |
| `implements` | code → feature or spec | `gov:feature`, the code record | `implemented-by` | P33 | feature to code |
| `tests` | test → code or feature | the test's own declaration | `tested-by` | P33 | coverage |
| `decides` | decision → node, a commit or an item among them | the decision row; `Decided:` trailers | `decided-by` | P33, its targets widened | decision to feature and commit |
| `instructs` | instruction unit → step, item, role, feature | the unit's `select` | `instructed-by` | P33 | instruction to work |
| `enforces` | gate or hook → unit or practice | the leg's or hook's fields | `enforced-by` | P33 | rule to gate |
| `after` | build → build; session → session, through resume and fork | the chain row; the binding | `before` | P33, its targets widened | order and lineage |
| `supersedes` | node → node it replaces | the new node | `superseded-by` | P33 | retirement |
| `amends` | node → node it changes | the amending node | `amended-by` | P33 | revision |
| `patches` | patch build → build or item | the patch build's intake | `patched-by` | P33 | Maintain's fixes |
| `owner` | node → chain build or layer | the node's declaration | `owns` | P33 | ownership |
| `layer` | kit or part → layer | the descriptor | `in-layer` | P33 | layers |
| `serves` | record, work order, commit → unit, item or build | the `**Serves:**` line; the `Gov-Unit:` and `Gov-Item:` trailers | `served-by` | new: today's Serves line, typed | record to unit (2,278 records), and commit to unit and item |
| `made-by` | commit, record → act or the owner | `Gov-Act:`; the record header | `made` | new | who made a thing |
| `caused-by` | record → the record or event that caused it | the record header's `**Caused-by:**` | `causes` | new | why a thing exists; the trace's spine |
| `follows` | act → work order | the act record | `followed-by` | new | under which instruction an act ran |
| `answers` | return → work order; the owner's answer → fork | the return's header; the answer's section | `answered-by` | new | return to handoff (prose in 58 of 88 research records) |
| `runs-in` | act, claim, commit → session | the session binding; a claim's `session:`; the `Gov-Session:` trailer | `hosts` | new | act and commit to session |
| `carries` | landing → unit, commit | the landing record | `carried-by` | new | what a landing moved |
| `pinned-at` | record, probe, claim → commit or tree | "Derived at", a probe's pin | `pinned-by` | new: today's pins, now typed apart from `cites` | staleness |
| `reads` | item, role → record kind | the kind's registry row | `read-by` | new | who reads a kind |
| `writes` | item, role → record kind | the kind's registry row | `written-by` | new | who writes a kind |
| `promoted-from` | instruction unit → memory node | `instructions.edit`'s change record | `promoted-to` | new | memory to instruction (no route today) |
| `cites` | any text → any node | derived from the text | `cited-by` | derived | prose references |

An unregistered type reds, and so does an edge whose source or target sits outside its row's namespaces.

## [cycle] The cycle, walked by key

Each hop of the owner's cycle, today and once the plan lands. "Typed" means a key reaches the next node; "search"
and "prose" mean it does not.

| Hop | From | To | Edge | Today | Planned site |
|---|---|---|---|---|---|
| charter practice → feature-scoped units | instruction | instruction | `instructs` | prose | the unit's `select` naming `feature.<name>` |
| units → work order | instruction | instruction | `instructs` | partly typed: `rules:` on role definitions | the work order's rendered slots, by tag |
| work order → act | instruction | runtime | `follows` | none | the act record's `task-sha` |
| act → session | runtime | runtime | `runs-in` | none: the run claim carries a session in prose | the session binding |
| act → commit | runtime | git | `made-by` | search: by SHA across transcripts | the `Gov-Act:` trailer |
| commit → unit and item | git | trail | `serves` (through `Gov-Unit:` and `Gov-Item:`) | partly typed: the subject's scope, unchecked | `Gov-Unit:` and `Gov-Item:` trailers |
| commit → landing | git | trail | `carries` | none: landing records are designed | the landing record |
| landing → verdict | trail | trail | `caused-by` | none | the verdict record's parent |
| return → work order | trail | instruction | `answers` | prose: in most research records | the return's header |
| record → unit | trail | trail | `serves` | typed, and graded both ways | the Serves line, as today |
| finding → bug class | trail | library | `caused-by` | none: `from:` on 0 of 149 | the class's header |
| decision → feature, commit | library | git | `decides` | none: on 199 of 200 rows | the row's edge line; `Decided:` trailers |
| bug class, decision → unit | library | instruction | `promoted-from` | none: no route | `instructions.edit` |
| feature → code | library | code | `part-of`, `implements` | typed at kit level | annotations and claims |

The loop closes at promotion: a lesson in the library becomes an instruction unit that names its source, and the
next work order that unit selects carries it.

## [sessions] Session ids, and what Codex can do

A session id addresses three things: a resumable conversation, its transcript, and, on Claude, a live inbox. The
plan keeps each where its writer keeps it and joins them by the act.
- **The act is the key that does not depend on the harness.** The supervisor mints it at launch and records beside
  it the harness, the node and the harness's session id (`--session-id` presets it on Claude). Journal lines,
  returns, commit trailers and records carry the act. Committed memory carries the act and, beside it, the harness
  session id, since the owner chose `trace.identity: session` (the away pass's AP-8). dLoggedFlight's run log keeps
  its closed schema, whose leg refuses session ids (`memory/builds/dLoggedFlight/README.md`, owner, 2026-09-13),
  until that leg reads the same key.
- **A session is a node derived from bindings.** It joins its act by `runs-in` and its predecessor by `after`, through
  a resume or a fork. Its transcript is a witness the binding points at; it never leaves its node, so another node
  renders it `not-local: node <x>`.
- **Inter-session messages are the mailbox first.** The durable copy is `refs/gov/mail/<slug>`, and the live copy
  goes to a session's inbox where the harness has one (`deps.messaging`). A script can resume, fork, read
  transcripts and list sessions (`claude agents --json`); only a model sends to another session's inbox.

| Capability | Claude Code | Codex |
|---|---|---|
| session id | preset at launch with `--session-id`, or returned in the JSON result (tested) | returned in the stream's start event; no preset (documented) |
| resume | `-p --resume <id>` (tested: it remembered) | `exec resume <id>` (help) |
| fork | `--fork-session` | interactive `fork` only |
| transcript | `~/.claude/projects/<cwd>/<id>.jsonl` (tested) | `~/.codex/sessions/.../rollout-<ts>-<id>.jsonl` (tested) |
| live inbox | per-session inbox, `SendMessage` (documented) | none found: the mailbox alone |
| hooks | the events gov wires today | twelve events, trusted by hash before they run (documented) |

So Codex can do the same for ids, resume and transcripts, and joins inter-session traffic through the mailbox
(`research-harness-cli.md` sections 3 and 5).

## [doors] Writing and reading

**Writing.** Five doors, one per site kind, and nothing else writes a node:
- `instructions.edit` writes instruction units and their change records, promotion included;
- `record` writes every record, its header and its edge lines, and refuses a missing `caused-by` on a kind that is
  not a root (intake, session binding, cadence lease);
- the commit queue writes the trailers from the act binding, and `prepare-commit-msg` fills them in the owner's own
  session;
- the handoff renderer writes work orders with their marker;
- the supervisor writes acts and session bindings.

**Reading.** One index answers every read:
- `gov tag show | where | refs | bundle <address>` returns a node, its location, its inbound edges, or its bundle
  (P33);
- `gov trace <key>` walks `caused-by` down from any key into a timeline, and `gov why <key>` walks up to the
  instruction units and the request behind it (the away pass's `[p5-observe]`);
- the card and every work order render their slots from the index, by tag;
- the atlas draws the families, the pockets and the edges from the records this plan names (`[view]`).

## [integration] Where the plan lands in the architecture

| Layer | What the plan adds |
|---|---|
| instruction | the shared edge grammar; the record header and section edge line as the instruction unit's twin; the eleven edge types registered; `promoted-from` on promotion |
| flow | the commit node and its trailer keys; one reader for `Pass:`, whose two readers disagree today; `carries` on landings |
| roles | every work order marked; `reads` and `writes` from role definitions; `answers` on every return |
| memory | the registry's rows gain home, lifecycle, readers and layer; witness rows for pockets outside the tree; the `caused-by` field on every kind; view, registry, archive and instrument kinds; the Serves backfill |
| runtime | the act as the key; session bindings with their pointers; journal lines keyed; the commit queue's trailers; the trace verbs |
| observability | readings over the journal and the commit keys; the Loop Review priced from trace rows |
| integrations | an artifact publication recorded as a release; adopters' remote trackers joined as witnesses |
| distribution | the Serves backfill and the edge lines as an update's upgrade step in each adopter |

## [chain] The units, by build

The plan's units live in v2 `[chain]`, one clause each. Each row below names the build whose row holds one, and the
clause by its opening words. The design map's chain-echo arm reds when a row's build holds no clause opening so.

| Build | The plan's part | Its v2 clause opens with |
|---|---|---|
| dOrderedCharter | the edge grammar, the eleven types, `promoted-from` and the edge checks | the shared edge grammar at every site the memory plan names |
| dOrderedCharter | the writing practice's checks | the one writing practice's checks over records as well as units |
| dDeclaredLoop | the commit node, its kind and its trailer keys | the commit node and its kind |
| dTotalRecall | the completed kind registry and the new kinds | the kind registry completed |
| dTotalRecall | `record`'s header and edge line, and the legacy records' reading | `record` writing each record's header |
| dLinkedLibrary | the decision and bug-class edges | `decides` on every decision row |
| dBoundRoles | markers on work orders, `answers` on returns | every work order carrying its marker |
| dWellOiledMachine | the act as the key | the act as the key |
| dWellOiledMachine | the commit queue's trailers and the commit-key leg | the commit queue writing the `Gov-*` trailers |
| dWellOiledMachine | the session node and live delivery | the session node derived from bindings |
| dPlacedRequest | the kickoff manifest as instruction units | the kickoff manifest's facts |
| dShippedRelease | `carries` on landings, and publications | `carries` on the landing record |
| dConvergedCharter | the guides' migration to tags | the guides' positional citations migrated to tags |

The atlas's memory view, derived from this record and the kind registry, was built in the away pass itself and
belongs to no chain build.

## [migration] Today's memory onto the plan

Nothing is rewritten by hand. Each step is mechanical, owned and graded:
- **Serves lines** become `serves` edges by reading, with no file changed.
- **Untagged headings** get derived anchors, frozen as aliases, so a legacy section is addressable without a retag;
  `memory.legacy-anchors` says whether an adopter derives anchors, the default, retags its records, or keeps neither.
- **Decision rows** gain `decides` from the dossiers that already list them, then by hand where none does, each a
  row of the decision kind's ledger population.
- **Old commits** stay as they are. The index reads what they carry, the subject's scope, `Pass:` and `Decided:`,
  and marks every edge it derives that way as derived.
- **Transcripts and the auto-memory** move nowhere. Bindings point at transcripts from the first act onward, and the
  auto-memory's standing directives are promoted as MS-1 settled.
- **In an adopter**, the backfill runs as an update's upgrade step, as the backlog migration does (NP-22).

## [gates] The checks the plan arms

Each is seen red on a planted case before it is trusted:
- **edges:** an unregistered type; a target that resolves nowhere; a source or target outside the type's namespaces;
  an inverse not rendered;
- **causes:** a non-root record with no `caused-by`; an orphan, a record nothing reaches from a root;
- **commits:** a pushed commit an act made with no `Gov-Act:`; a `Gov-Act:` the binding does not hold; a planted
  `Gov-Item:` trailer read as anything but `serves`;
- **work orders:** a handoff with no marker; a return with no `answers`;
- **positional:** a new positional citation in live text;
- **pins:** a quoted derived fact with no pin on its line, across every record;
- **promotion:** a standing directive found in memory and not promoted, as the auto-memory's measure already reads.

## [view] The atlas's memory view

The atlas gains a Memory view, derived and never typed. It draws:
- the eight families of `[families]`, as one ring in the cycle's order, each listing its pockets;
- every pocket of `[pockets]`, with its status (node, witness, out), its owner and its key;
- the kind registry's record kinds (layer-memory `[contract]`), each placed on the step or program of the first writer
  item its row names, or shown apart under its declared marker (no writer item, writer item not named, every step's
  exit item), with its owner;
- the closed edge set of `[edges]`, each type with its declaring site and its inverse;
- the cycle of `[cycle]`, each hop marked typed or not today.

Clicking a pocket, a kind or an edge opens its detail. The view reads this record and layer-memory, so a change to
either moves it. It refuses what it cannot place: a kind with neither a writer item nor a marker, a writer token that
resolves to no item, key or file, an unread status or state, an undeclared hop edge, and a table split by a blank
line, each seen red on a planted case.

## [keys] The keys the plan adds

| Key | Allowed values | Default | Why |
|---|---|---|---|
| `memory.legacy-anchors`, widened | derived, none, retag | derived | the systems round's key gains `retag`: an adopter's own records are its own, and the default rewrites no file |
| `commits.edge-check` | push-leg, commit-msg, off | push-leg | a refusal at commit time catches the owner's own commits mid-thought; the push is the binding boundary |
| `commits.squash` | re-emit-union, refuse, accept-loss | re-emit-union | a squash drops every trailer; gov never squashes, an adopter may |
| `trace.identity` | act-only, session, salted | session | the owner's AP-8: committed memory may name the harness session id beside the act |
